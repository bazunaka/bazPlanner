   M S B A M L   `   `   `  ����H  DbazPlannerWPF, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null-clr-namespace:bazPlannerWPFbazPlannerWPF  5   	       bazPlannerWPF.MainWindow   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   -localclr-namespace:bazPlannerWPF     5   	   _ [MaterialDesignThemes.Wpf, Version=4.5.0.0, Culture=neutral, PublicKeyToken=df2a72020bd7962aFmaterialDesign1http://materialdesigninxaml.net/winfx/xaml/themes  5   	     � Title$  bazPlanner-WPF version��5	   	   $	��550��6(   $	��800��68   $	��550��6H   $	��800��6U   .��5
      � -   5         �Name$ GridMain��5
         StyleForMainWimdow#��[  6    � RowDefinitions 5   
   �� 5      -   5         ��Name$ Header��5      $
��Auto �6,    � Language$ ru-ru�6:   $��30��6K   �� 5      -   5        $ Content��5      $ ru-ru�6-   �� 5      -   5        $ Bottom��5      $��30 �6,   $ ru-ru�68   .+�5   
   o� $��25��6   $
��Left=�6   $
��auto��66   .@�5      m� -   5        $��Главное меню��5      $��25��6-   .@�5      m� -   5        $$��Подключение к БД��5      65   m� 5      -   5         m�Name$ menuCreateProject��5   ^   $!��Создать проект��6   {�.  6^   m� 5      -   5        $ menuCreateTask��5   ^   $!��Создать задачу��6   {�.  6^   5      m� 5      $��	Меню2��6   $��25��6&   {�.  62   m� 5      $��	Меню3��6   $��25��6&   {�.  62   m� 5      $��	Меню4��6   $��25��6&   {�.  62   5      �� 5   
   -	   5         ��Name$ StackTop��5      $��0��6'   $��Right=�64   $
��auto��6P   .+�5      �� -
   5         ��Name$ 	labelAuth��5   .   $��25��6   $��14(�6    $	��252��6A   $G��AНезарегистрированный пользователь��6M   $��Right=�6y   5      ]� 5   
   $��1��6   .+�5      &   System.Windows.Controls.Calendar  -   5          Name$ PresentMonth��5   #   $	��250��6   $��Right=�69   $	��330��6P   $	��Top=�6]   	 � Language$	 ru-ru�6u   �� 5      -   5        
 ��Name$
 listElements��5   h   $	��200��6   $
��Left=�6M   6h   (  "System.Windows.Controls.DatePicker  5       $	��148��6   $	��155��6%   5!      �� 5"   
   -   5        $ StackBottom��5"      $��2��6*   .+�5#      �� $
��auto��6   $��Stretch=�6&   $
��auto��6K   .@�5$      �� -   5        $ Now_time��5$   N   $��25��6   $��Right=�6$   $��14(�6@   $��2��6`   5%      5&      5'      5(      