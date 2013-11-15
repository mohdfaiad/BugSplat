program GameMain;
uses SwinGame, sgTypes, SysUtils;

procedure Main();
var
  bug: Sprite;
begin
  OpenAudio();
  
  OpenGraphicsWindow('Bug Splat', 1024, 768);
  LoadDefaultColors();
  ShowSwinGameSplashScreen();

  LoadResourceBundle('BugSplat.txt');

  bug := CreateSprite('Buggy', 'BuggyAnimations');
  SpriteSetPosition(bug, RandomScreenPoint());
  SpriteMoveTo(bug, RandomScreenPoint(), 1 + Rnd(10));

  repeat
    ProcessEvents();
    
    DrawBitmap('Background1', 0, 0);
    DrawAllSprites();
    RefreshScreen(60);

    UpdateAllSprites();
  until WindowCloseRequested();
    
  CloseAudio();
  ReleaseAllResources();
end;

begin
  Main();
end.
