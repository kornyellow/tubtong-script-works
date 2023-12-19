for file in *.mp3; do
  title=$(basename "$file" .mp3)
  id3v2 --song "$title" --album "เพลงการแสดงปีใหม่ทับทอง" --artist "โรงเรียนทับทอง" "$file"
done
