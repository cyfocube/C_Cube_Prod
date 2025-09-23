#!/bin/bash
# C-Cube Video Player Script
# Plays videos with audio using available macOS tools

VIDEO_FILE="$1"
PLAYER_CHOICE="$2"

if [ -z "$VIDEO_FILE" ]; then
    echo "❌ Usage: $0 <video_file> [player_choice]"
    echo "📁 Available videos in output folder:"
    ls -la "/Users/oladimejishodipe/Desktop/Cold_Wallet copy 2/video_generator/output/"*.mp4 2>/dev/null | head -10
    exit 1
fi

if [ ! -f "$VIDEO_FILE" ]; then
    echo "❌ File not found: $VIDEO_FILE"
    exit 1
fi

echo "🎥 C-Cube Video Player"
echo "📁 Playing: $(basename "$VIDEO_FILE")"
echo "🔊 Audio: Enabled"

# Method 1: QuickTime Player (Default macOS)
play_with_quicktime() {
    echo "▶️  Opening with QuickTime Player..."
    open -a "QuickTime Player" "$VIDEO_FILE"
}

# Method 2: macOS open command (lets system choose)
play_with_default() {
    echo "▶️  Opening with default application..."
    open "$VIDEO_FILE"
}

# Method 3: VLC if available
play_with_vlc() {
    if command -v vlc &> /dev/null; then
        echo "▶️  Opening with VLC..."
        vlc "$VIDEO_FILE" --intf macosx --play-and-exit
    else
        echo "⚠️  VLC not found, trying QuickTime..."
        play_with_quicktime
    fi
}

# Method 4: ffplay if available
play_with_ffplay() {
    if command -v ffplay &> /dev/null; then
        echo "▶️  Playing with ffplay..."
        ffplay -autoexit -window_title "C-Cube Video Player" "$VIDEO_FILE"
    else
        echo "⚠️  ffplay not found, trying QuickTime..."
        play_with_quicktime
    fi
}

# Choose player based on preference
case "$PLAYER_CHOICE" in
    "vlc")
        play_with_vlc
        ;;
    "ffplay")
        play_with_ffplay
        ;;
    "quicktime")
        play_with_quicktime
        ;;
    *)
        echo "🎯 Trying best available player..."
        # Try in order of preference
        if command -v vlc &> /dev/null; then
            play_with_vlc
        elif [ -d "/Applications/QuickTime Player.app" ]; then
            play_with_quicktime
        else
            play_with_default
        fi
        ;;
esac

echo "✅ Player launched successfully!"
echo "💡 If no audio, check:"
echo "   🔊 System volume"
echo "   🔊 Player volume controls"
echo "   🔊 macOS Privacy & Security settings"