using System;
using System.Windows;
using static bazPlannerWPF.DBConnect;
using static bazPlannerWPF.Owner;

namespace bazPlannerWPF
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            DateTime now = DateTime.Now;
            Now_time.Content = now.ToString("D");
            
            if(DBConnect.Connect("test.db"))
            {
                Console.WriteLine("Connected!");
            }

            PresentMonth.SelectedDate = DateTime.Now;
            NextMonth.SelectedDate = DateTime.Now.AddMonths(+1);
            TwoNextMonth.SelectedDate = DateTime.Now.AddMonths(+2);

            //File.AppendAllText("log.txt", Environment.NewLine); логирование потом!
        }

        private void Connect_to_DB(object sender, RoutedEventArgs e)
        {
            if(CheckAuth() == 0)
            {
                create_user newUser = new create_user();
                newUser.Show();
            }
            else
            {
                CheckAdmin();
            }
        }

        private void Create_project(object sender, RoutedEventArgs e)
        {
            create_project newProject = new create_project();
            newProject.Show();
        }

        private void Create_task(object sender, RoutedEventArgs e)
        {
            create_task newTask = new create_task();
            newTask.Show();
        }
    }
}
