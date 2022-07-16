using System;
using System.Windows;
using static bazPlannerWPF.DBConnect;

namespace bazPlannerWPF
{
    public partial class MainWindow : Window
    {

        public MainWindow()
        {
            InitializeComponent();
            DateTime now = DateTime.Now;
            Now_time.Content = now.ToString("D");

            if (Connect("test.db"))
            {
                Console.WriteLine("Connected!");
            }
            else
            {
                Console.WriteLine("Not connected!");
            }

            //PresentMonth.SelectedDate = DateTime.Now;

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
                Auth formAuth = new Auth
                {
                    Owner = this
                };
                formAuth.Show();
            }
        }

        private void Create_project(object sender, RoutedEventArgs e)
        {
            Create_project newProject = new Create_project();
            newProject.Show();
        }

        private void Create_task(object sender, RoutedEventArgs e)
        {
            create_task newTask = new create_task();
            newTask.Show();
        }

        private void MenuItem_Click(object sender, RoutedEventArgs e)
        {

        }
    }
}
